Random notes & poorly written Go code to solve https://www.serverheist.com/
(SH), but mostly to learn Go.

Yeah I know I haven't even gotten halfway through AoC 2021. I'll get there.
Someday.

# Challenge 1: `login`

Unlike AoC which starts off with several trivial warm-up exercises, SH hits you
away with a meaty puzzle already. I don't mind that, but the ergonormics in SH
leave a lot to be desired:

- It doesn't seem to remember my progress, so when I came back to the site this
  morning, I had to do everything again (email validation, login, enter correct
  password).

- This is extra annoying because the password list is randomly generated every
  time, and the site hijacks both ctrl+c and right click, so I had to copy the
  xhr response from the network inspector instead. Maybe it's intentional so I
  realize the repeated failing requests to some `serverheist-hacker.tk` server.
  Or maybe automating the tedious steps is part of the challenge as well. Idk,
  it starts to feel a bit too much like actual work for me.
