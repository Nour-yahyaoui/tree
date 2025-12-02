# Masrouf

Everything lives in localStorage, so there is nothing to deploy.

## Decision

Amounts are integers in minor units, never floats.

## Why

The page redraws from the store on every change, which is cheap at this size.

## How

Amounts are integers in minor units, never floats.
