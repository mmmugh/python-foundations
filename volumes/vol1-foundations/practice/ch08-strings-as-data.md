## Practice: a log line parser

A server writes a line every time something happens, and by Friday there are
forty thousand of them. Each line looks like this:

```
WARN|14:03|Disk usage at 91 percent
```

Three fields separated by `|`: the level, the time, and the message. The
message never contains a `|`. You are going to write the functions that pull a
line apart, and then one that finds the lines worth reading.

Everything here uses Chapters 1 to 8: lists, loops, and now `split()`,
`join()`, `upper()`, `strip()`, `replace()`, `isalpha()` and `str()`.

Real logs are untidy. Some lines come in with the level in lowercase and stray
spaces around the message, so a couple of these steps have to cope with that
rather than assume it away.

### Steps

1. Write `level_of(line)` returning the level, so `WARN` from the line above. Split on the separator rather than counting characters.
2. Write `time_of(line)` returning the time field.
3. Write `message_of(line)` returning the message field.
4. Write `is_warning(line)` returning `True` for a warning and `False` otherwise. It must say `True` for `warn` in lowercase too, because half the services write it that way.
5. Write `tidy(line)` returning the line rebuilt with the level in uppercase and the message stripped of leading and trailing spaces, still separated by `|`. Use `join()` to put it back together.
6. Write `words_in(message)` returning a list of the message's words that are made only of letters, so `Disk usage at 91 percent` loses the `91`.
7. Write `redact(line, word)` returning the line with every appearance of that word replaced by `****`.
8. Write `warning_messages(lines)`, given a list of lines, returning just the messages of the warnings — not the whole lines, and not the other levels.
