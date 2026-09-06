from playwright.sync_api import Page, expect


def test_home_page(Page):
    Page.goto("http://127.0.0.1:8000/")
    Page.get_by_text("Login").click()
    Page.locator('[name="username"]').fill("hamedx")
    Page.locator('[name="password"]').fill("hH19921992@")
    Page.get_by_role('button', name="Login").click()
    #page.pause()

    expect(Page).to_have_title("GODSOFSTRATEGY")