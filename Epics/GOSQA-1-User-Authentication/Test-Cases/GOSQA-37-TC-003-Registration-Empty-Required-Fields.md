# GOSQA-37 – TC-003: Verify Registration Fails When Required Fields Are Left Empty

## Epic

**GOSQA-1 – User Authentication**

---

## Related Story

**GOSQA-26 – Register a New User Account**

---

## Objective

Verify that the system prevents user registration when one or more required fields are left empty.

---

## Preconditions

- GOSQA-38 – User is not logged in.
- GOSQA-39 – Registration page is accessible.

---

## Test Steps

| Step | Action | Test Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Open the registration page. | URL: `/register` | Registration page is displayed successfully. |
| 2 | Leave all required fields empty. | Username: Empty<br>Email: Empty<br>Password: Empty | No input is entered into the required fields. |
| 3 | Click the **Register** button. | — | Registration request is blocked and validation is triggered. |

---

## Expected Result

- Registration is not completed.
- No new user account is created.
- Validation messages are displayed for all required fields.

---

## Traceability

### Related Story

- GOSQA-26 – Register a New User Account

### Related Preconditions

- GOSQA-38
- GOSQA-39

---

## Priority

Highest

---

## Status

Completed

---

## Jira Reference

- Epic: **GOSQA-1**
- Story: **GOSQA-26**
- Test: **GOSQA-37**