import * as fs from 'fs';
import * as path from 'path';

/**
 * Post-process the openapi-generator pom.xml so the Java SDK can be published to
 * Maven Central (Sonatype Central Portal) under the `com.eulerstream` namespace.
 *
 * The generated pom ships with OpenAPITools placeholder metadata (url, scm,
 * licenses, developers) and no publishing plugin, and Central rejects artifacts
 * that are missing required POM metadata or are unsigned. Because the generated
 * tree is wiped and recreated on every build, this runs as a codegen step rather
 * than being committed once. It:
 *
 *   - sets the project <version> from version.txt (the persisted source of truth,
 *     which lives OUTSIDE the regenerated tree so it survives regeneration),
 *   - replaces the placeholder name/description/url/scm/licenses/developers with
 *     EulerStream's,
 *   - adds the central-publishing-maven-plugin (auto-publish on validation) and
 *     skips the default deploy plugin, and
 *   - rewrites the sign-artifacts profile's GPG plugin to sign non-interactively
 *     (loopback pinentry) in CI.
 */

const POM_PATH = path.resolve(__dirname, '..', 'src/generated/pom.xml');
const VERSION_PATH = path.resolve(__dirname, '..', 'version.txt');

const GROUP_ID = 'com.eulerstream';
const ARTIFACT_ID = 'euler-api-sdk';
const REPO_URL = 'https://github.com/EulerStream/EulerApiSdk';

const version = fs.readFileSync(VERSION_PATH, 'utf-8').trim();
let pom = fs.readFileSync(POM_PATH, 'utf-8');

function replaceFirst(re: RegExp, replacement: string, label: string): void {
    if (!re.test(pom)) {
        throw new Error(`fix-pom: could not find ${label} to replace (pattern ${re}).`);
    }
    pom = pom.replace(re, replacement);
}

// Project coordinates. The first <groupId>/<version> in document order are the
// project's own (dependency/plugin coordinates appear later, inside <build>).
replaceFirst(/<groupId>[^<]*<\/groupId>/, `<groupId>${GROUP_ID}</groupId>`, 'project groupId');
replaceFirst(/<version>[^<]*<\/version>/, `<version>${version}</version>`, 'project version');

// Project metadata required by Maven Central.
replaceFirst(/<name>[^<]*<\/name>/, `<name>${ARTIFACT_ID}</name>`, 'project name');
replaceFirst(
    /<url>[^<]*<\/url>/,
    `<url>${REPO_URL}</url>`,
    'project url',
);
replaceFirst(
    /<description>[^<]*<\/description>/,
    '<description>Official EulerStream API SDK for Java — TikTok LIVE signing and API client.</description>',
    'project description',
);
replaceFirst(
    /<scm>[\s\S]*?<\/scm>/,
    [
        '<scm>',
        `        <connection>scm:git:${REPO_URL}.git</connection>`,
        `        <developerConnection>scm:git:${REPO_URL}.git</developerConnection>`,
        `        <url>${REPO_URL}</url>`,
        '    </scm>',
    ].join('\n'),
    'scm',
);
replaceFirst(
    /<licenses>[\s\S]*?<\/licenses>/,
    [
        '<licenses>',
        '        <license>',
        '            <name>MIT License</name>',
        '            <url>https://opensource.org/licenses/MIT</url>',
        '            <distribution>repo</distribution>',
        '        </license>',
        '    </licenses>',
    ].join('\n'),
    'licenses',
);
replaceFirst(
    /<developers>[\s\S]*?<\/developers>/,
    [
        '<developers>',
        '        <developer>',
        '            <id>eulerstream</id>',
        '            <name>EulerStream</name>',
        '            <url>https://www.eulerstream.com</url>',
        '        </developer>',
        '    </developers>',
    ].join('\n'),
    'developers',
);

// Publishing plugins: add the Central Portal publisher and skip the default
// deploy plugin (it would otherwise fail with no distributionManagement). Insert
// before the first </plugins> (the main <build>, not the profile build).
const publishingPlugins = [
    '            <plugin>',
    '                <groupId>org.sonatype.central</groupId>',
    '                <artifactId>central-publishing-maven-plugin</artifactId>',
    '                <version>0.7.0</version>',
    '                <extensions>true</extensions>',
    '                <configuration>',
    '                    <publishingServerId>central</publishingServerId>',
    '                    <autoPublish>true</autoPublish>',
    '                    <waitUntil>published</waitUntil>',
    '                </configuration>',
    '            </plugin>',
    '            <plugin>',
    '                <groupId>org.apache.maven.plugins</groupId>',
    '                <artifactId>maven-deploy-plugin</artifactId>',
    '                <version>3.1.1</version>',
    '                <configuration>',
    '                    <skip>true</skip>',
    '                </configuration>',
    '            </plugin>',
    '        </plugins>',
].join('\n');
replaceFirst(/<\/plugins>/, publishingPlugins, 'main build </plugins>');

// Sign artifacts non-interactively in CI. setup-java provides the passphrase via
// the `gpg.passphrase` server in settings.xml; loopback pinentry lets gpg read it
// without a TTY. Replace the whole profile so the config is deterministic.
replaceFirst(
    /<profiles>[\s\S]*?<\/profiles>/,
    [
        '<profiles>',
        '        <profile>',
        '            <id>sign-artifacts</id>',
        '            <build>',
        '                <plugins>',
        '                    <plugin>',
        '                        <groupId>org.apache.maven.plugins</groupId>',
        '                        <artifactId>maven-gpg-plugin</artifactId>',
        '                        <version>3.2.1</version>',
        '                        <executions>',
        '                            <execution>',
        '                                <id>sign-artifacts</id>',
        '                                <phase>verify</phase>',
        '                                <goals>',
        '                                    <goal>sign</goal>',
        '                                </goals>',
        '                            </execution>',
        '                        </executions>',
        '                        <configuration>',
        '                            <gpgArguments>',
        '                                <arg>--pinentry-mode</arg>',
        '                                <arg>loopback</arg>',
        '                            </gpgArguments>',
        '                        </configuration>',
        '                    </plugin>',
        '                </plugins>',
        '            </build>',
        '        </profile>',
        '    </profiles>',
    ].join('\n'),
    'sign-artifacts profile',
);

fs.writeFileSync(POM_PATH, pom, 'utf-8');
console.log(
    `Patched ${POM_PATH}: ${GROUP_ID}:${ARTIFACT_ID}:${version} ` +
    '(Central Portal publishing + metadata + signing).',
);
