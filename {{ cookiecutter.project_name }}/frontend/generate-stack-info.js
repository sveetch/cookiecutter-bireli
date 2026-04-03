#!/usr/bin/env node
/**
 * Generate node_stack.json for stack info page.
 * Run this during CI build to cache Node.js stack information
 * for environments where Node.js is not available at runtime.
 *
 * Usage: node generate-stack-info.js
 * Output: ../parts/node/node_stack.json
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Get Node.js version
let nodeVersion = null;
try {
    nodeVersion = process.version;
} catch (e) {
    console.error('Could not get Node.js version');
}

// Get npm version
let npmVersion = null;
try {
    npmVersion = execSync('npm --version', { encoding: 'utf8' }).trim();
} catch (e) {
    console.error('Could not get npm version');
}

// Read packages from package.json
let packages = [];
try {
    const packageJsonPath = path.join(__dirname, 'package.json');
    const packageData = JSON.parse(fs.readFileSync(packageJsonPath, 'utf8'));

    const deps = packageData.dependencies || {};
    const devDeps = packageData.devDependencies || {};

    for (const [name, version] of Object.entries(deps)) {
        packages.push({ name, version, dev: false });
    }

    for (const [name, version] of Object.entries(devDeps)) {
        packages.push({ name, version, dev: true });
    }

    // Sort packages by name
    packages.sort((a, b) => a.name.toLowerCase().localeCompare(b.name.toLowerCase()));
} catch (e) {
    console.error('Could not read package.json:', e.message);
}

// Build stack info object
const stackInfo = {
    node_version: nodeVersion,
    npm_version: npmVersion,
    packages: packages,
    generated_at: new Date().toISOString()
};

// Ensure output directory exists
const outputDir = path.join(__dirname, '..', 'parts', 'node');
if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
}

// Write to file
const outputPath = path.join(outputDir, 'node_stack.json');
fs.writeFileSync(outputPath, JSON.stringify(stackInfo, null, 2));

console.log(`Node.js stack info written to: ${outputPath}`);
console.log(`  Node.js: ${nodeVersion}`);
console.log(`  npm: ${npmVersion}`);
console.log(`  Packages: ${packages.length}`);
