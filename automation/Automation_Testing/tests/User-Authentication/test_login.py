from playwright.sync_api import Page, expect


def test_successful_user_login(page: Page):
    page.goto("http://127.0.0.1:8000/")
    page.get_by_text("Login").click()
    page.locator('[name="username"]').fill("hamedx")
    page.locator('[name="password"]').fill("hH19921992@")
    page.get_by_role('button', name="Login").click()
   
    expect(page).to_have_url("http://127.0.0.1:8000/profile/")
    #page.pause()





def test_login_with_invalid_username(page: Page):
    page.goto("http://127.0.0.1:8000/login")
    page.locator('[name="username"]').fill("bambo")
    page.locator('[name="password"]').fill("hH19921992@")
    page.get_by_role('button', name="Login").click()

    expect(page.get_by_text("Invalid username or password.")).to_be_visible()
    expect(page).to_have_url("http://127.0.0.1:8000/login/")
    print(page.url)
    #page.pause()