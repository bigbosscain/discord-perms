# discord command permission helper

this is a small helper i use to keep command permission checks out of my command code

instead of checking user ids and role ids inside every command, this puts all of that logic in one place and keeps things consistent

## what it handles

- owner overrides
- specific users who are allowed
- roles that are allowed
if any of those match, the command is allowed to run

## how it works

you create one `CommandPermissionHelper` instance with the ids you care about
when a command runs, you pass in the user id and a list of their role ids

if `can_run` returns true, the command can execute
if it returns false, you block it

it does not depend on any specific discord library
you just pass in plain ints

## why this exists

i got tired of copy-pasting permission checks into every command
this keeps that logic in one place and makes command code easier to read and change later

## scope

this is intentionally small.
it is not a full permissions system or framework
it just solves one problem and stays out of the way

## install

copy `permissions.py` into your project
there are no external dependencies

## license

mit
