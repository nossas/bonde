// eslint-disable-next-line no-undef
module.exports = {
  coverageReporters: ["lcov", "text-summary"],
  roots: [
    "<rootDir>/packages/accounts-client/src",
    "<rootDir>/packages/admin-client/src",
    "<rootDir>/packages/canary-client/src",
    // "<rootDir>/packages/redes-client/src",
    "<rootDir>/packages/webpage-client/src"
  ],
  testMatch: [
    "**/__tests__/**/*.+(ts|tsx|js)",
    "**/?(*.)+(spec|test).+(ts|tsx|js)",
  ],
  transform: {
    "^.+\\.(js|jsx|ts|tsx)$": "ts-jest",
  },
  moduleNameMapper: {
    // Handle CSS imports (with CSS modules)
    // https://jestjs.io/docs/webpack#mocking-css-modules
    "^.+\\.(css|sass|scss)$": "identity-obj-proxy",

    // Handle image imports
    // https://jestjs.io/docs/webpack#handling-static-assets
    "^.+\\.(jpg|jpeg|png|gif|webp|avif|svg)$": `<rootDir>/__mocks__/style.js`,
  },
  transformIgnorePatterns: [
    "/node_modules/",
    "^.+\\.module\\.(css|sass|scss)$",
  ],
  testPathIgnorePatterns: [
    "<rootDir>/packages/webpage-client/node_modules/",
    "<rootDir>/packages/webpage-client/.next/",
    "<rootDir>/packages/webpage-client/cypress-tpackages/admin-client/src/jest/mock-style.jsests/",
  ],
  setupFilesAfterEnv: ["<rootDir>/packages/webpage-client/src/setupTests.ts"]
};
