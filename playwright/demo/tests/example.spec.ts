import { test, expect } from '@playwright/test';

test('Basic Test Example', async ({ page }) => {
  await page.goto('https://ray.run/');
  const pageTitle = await page.title();
  expect(pageTitle).toBe('Ray Run - The Ultimate Platform');
});