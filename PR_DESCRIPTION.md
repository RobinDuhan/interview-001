# PR #142 — Add product search + admin restock

**Author:** @new-grad-dev (SDE-1) · **Reviewers:** you
**Branch:** `pr/product-search-admin` → `main`

## What this does

Two things marketing and ops asked for:

1. **`GET /products/search?q=<text>&sort=<expr>`** — search the catalog by
   product name. Also applies our standard 10% storefront discount to the
   price in the response. Supports custom sorting (e.g. `sort=price desc`).
2. **Admin endpoints** — `POST /admin/restock` to add stock, and
   `DELETE /admin/products/{id}` to remove a product. Restock is protected by
   an admin token.

## Testing

- Added `tests/test_06_search.py` — searching for "Mouse" returns a result. ✅
- Manually tested restock in my local env, works great.

## Notes

- First time touching SQLAlchemy raw queries, LMK if the search query looks
  off but it worked when I tried it.
- Left the admin token in the code for now with a TODO — can move it to config
  in a follow-up PR.

---

### Reviewer instructions (for the interview)

Review this PR as if it landed in your queue. Talk through:

- Anything you'd **block the merge** on, and why.
- Severity of each issue (what's a security hole vs. a nit).
- What you'd ask the author to change, and how you'd fix the worst one.

You do not need to run it. Read it like a real review.
