# GOSQA-41 – TC-005: Verify Login Fails with an Incorrect Password

## Epic

**GOSQA-1 – User Authentication**

---

## Related Story

**GOSQA-27 – Authenticate Users and Provide Account Access**

---

## Objective

Verify that the system prevents login when a registered user enters an incorrect password.

---

## Preconditions

- GOSQA-43 – A registered user account exists.
- GOSQA-44 – User is logged out.
- GOSQA-45 – Login page is accessible.

---

## Test Steps

| Step | Action | Test Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Open the login page. | | Login page is displayed successfully. |
| 2 | Enter a valid username. | `hamed123` | Username is accepted. |
| 3 | Enter an incorrect password. | `WrongPassword123!` | Password is accepted. |
| 4 | Click the **Login** button. | — | Authentication request is submitted. |

---

## Expected Result

- Authentication fails.
- The user is not granted access to the account.
- An appropriate error message is displayed indicating that the username or password is incorrect.

---

## Traceability

### Related Story

- GOSQA-27 – Authenticate Users and Provide Account Access

### Related Preconditions

- GOSQA-43
- GOSQA-44
- GOSQA-45

---

## Priority

Highest

---

## Status

Done

---

## Jira Reference

- Epic: **GOSQA-1**
- Story: **GOSQA-27**
- Test: **GOSQA-41**