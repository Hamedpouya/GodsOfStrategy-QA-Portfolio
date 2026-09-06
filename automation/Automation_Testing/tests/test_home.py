from playwright.sync_api import Page, expect


def test_home_page(page):
    page.goto("http://127.0.0.1:8000/")
    page.get_by_text("Login").click()
    page.locator('[name="username"]').fill("hamedx")
    page.locator('[name="password"]').fill("gvg55485fef")
    page.get_by_role('button', name="Login").click()
    #page.pause()

    expect(page).to_have_title("GODSOFSTRATEGY")