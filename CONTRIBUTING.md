Developer's guidelines
---

# Git workflow

We maintain an invariant that code in the `master` is not broken, therefore we employ the following workflow.

- Every feature has its own branch.
  Currently, it is `frontend` and `backend`.
- When the developement of a feature is deemed sufficient, send a pull request.
  Never push directly to `master`.
- We use tagged release from `master` when integration tests succeed.


# Coding convention

- Always use descriptive variable names.
- Never create files with spaces in their names, because this breaks a lot of things.
- Commit history is valuable, therefore try to adhere to [good style of commit messages](https://chris.beams.io/posts/git-commit/).


# Tests and CI
