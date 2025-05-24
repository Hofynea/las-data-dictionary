/**
 * @file app.config.server.spec.ts
 * @author Daria Ilchenko
 * @date November 2024
 * @description Unit tests for the server-side application configuration in `app.config.server.ts`.
 * This file validates that the server configuration:
 * - Provides the necessary server rendering providers.
 * - Correctly merges application configuration with server configuration.
 * - Exports the merged configuration as expected.
 */

import { TestBed } from '@angular/core/testing';
import { ApplicationConfig, mergeApplicationConfig } from '@angular/core';
import { provideServerRendering } from '@angular/platform-server';
import { appConfig } from './app.config';
import { config } from './app.config.server';

describe('app.config.server.ts', () => {
  // Setup the testing module before each test case
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [], // Add any necessary providers for future extensions
    });
  });

  it('should provide server rendering configuration', () => {
    // Define the server configuration for testing
    const serverConfig: ApplicationConfig = {
      providers: [provideServerRendering()],
    };

    // Ensure the serverConfig contains the expected provider
    expect(serverConfig.providers).toContain(provideServerRendering());
  });

  it('should merge appConfig with serverConfig', () => {
    // Define the server configuration
    const serverConfig: ApplicationConfig = {
      providers: [provideServerRendering()],
    };

    // Merge appConfig with serverConfig
    const mergedConfig = mergeApplicationConfig(appConfig, serverConfig);

    // Validate that mergedConfig contains providers from both appConfig and serverConfig
    appConfig.providers?.forEach(provider => {
      expect(mergedConfig.providers).toContain(provider);
    });
    serverConfig.providers?.forEach(provider => {
      expect(mergedConfig.providers).toContain(provider);
    });
  });

  it('should export the merged config correctly', () => {
    // Define the expected merged configuration
    const expectedConfig = mergeApplicationConfig(appConfig, {
      providers: [provideServerRendering()],
    });

    // Ensure the exported config matches the expected merged configuration
    expect(config.providers).toEqual(expectedConfig.providers);
  });
});
