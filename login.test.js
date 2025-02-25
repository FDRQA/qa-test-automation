const { test, expect } = require('@playwright/test');
const { LoginPage } = require('../pages/LoginPage');

test('Login exitoso en Internxt Drive', async ({ page }) => {
    const loginPage = new LoginPage(page);

    await loginPage.navigate();
    await loginPage.login('fatima@internxt.com', 'Morgana.79@');
    await loginPage.confirmLoginSuccess();
    await loginPage.openDesktopApp();

    console.log("✅ Aplicación de escritorio abierta exitosamente.");
});