# Masrouf

Amounts are integers in minor units, never floats.

## Decision

Everything lives in localStorage, so there is nothing to deploy.

## Why

Amounts are integers in minor units, never floats.

## How

The page redraws from the store on every change, which is cheap at this size.
