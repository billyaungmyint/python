// tests/google.spec.ts
import { test, expect } from "@playwright/test";

// page here will open a new browser
test("Page demo", async ({ page }) => {
  // set timeout to 2 sec
  test.setTimeout(2 * 1000);
  // opens the page to google URL
  await page.goto("https://google.com");
  // look for title=Search - textbox
  const input = page.locator("[title=Search]");
  await input.type("playwright");
  await input.press("Enter");
  //assert
  await expect(page).toHaveTitle("playwright - Google Search");

  // Never resolves. to pause the browser from closing at the end. just like time.pause in Python
  //   await new Promise(() => {});
});
