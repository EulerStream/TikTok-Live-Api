import { fileURLToPath } from "node:url";
import Client, { buildConfig } from "../src/index.js";
import * as Sdk from "../src/sdk/index.js";
import { runBasicTests } from "../../common/test/basic.js";

runBasicTests({
    Client,
    buildConfig,
    Sdk,
    manifestPath: fileURLToPath(new URL("./sdk-manifest.json", import.meta.url)),
    clientName: "TikTokApiSdk",
});
