import * as path from 'node:path';

/**
 * Build settings shared by every TypeScript SDK package. Paths resolve against
 * the folder tsdown runs in, which is the package folder.
 *
 * This is a plain object rather than a `defineConfig(...)` call so that this
 * folder needs no dependency on tsdown; each package's tsdown.config.ts wraps it.
 */
export const baseConfig = {
  entry: ['src/index.ts'],
  format: ['esm' as const],
  dts: true,
  sourcemap: true,
  clean: true,
  target: 'node18',
  platform: 'node' as const,
  alias: {
    '@': path.resolve(process.cwd(), 'src'),
  },
  outExtensions: () => ({ js: '.js', dts: '.d.ts' }),
  deps: {
    neverBundle: ['axios'],
  },
};
