import {Configuration} from "@/sdk";
import {AxiosRequestConfig} from "axios";

export type ClientConfiguration = Configuration & {
  apiKey?: string
}

export function buildConfig(baseConfig: Partial<ClientConfiguration>): ClientConfiguration {

  const config: ClientConfiguration = {
    ...{
      basePath: 'https://api.eulerstream.com', // Or your choice of alternate signature provider
      baseOptions: {validateStatus: () => true} as AxiosRequestConfig,
      isJsonMime: (mime: string) => mime.toLowerCase().includes("application/json")
    },
    ...baseConfig
  }

  if (!config.apiKey) {
    return config;
  }

  const apiKey = config.apiKey;
  delete config.apiKey;

  config.baseOptions.headers ||= {};
  config.baseOptions.headers['X-Api-Key'] = apiKey;

  return config;

}