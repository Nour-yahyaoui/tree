# The Money Page

Amounts are integers in minor units, never floats.

## Decision

Amounts are integers in minor units, never floats.

## Why

Everything lives in localStorage, so there is nothing to deploy.

## How

The page redraws from the store on every change, which is cheap at this size.
