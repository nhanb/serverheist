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

# Challenge 2: thecoup

Fine.

# Challenge 3: blackhat

`ps` didn't show anything that seems to be related to the repeated
serverheist-hacker.tk requests.

How the hell am I supposed to submit my code? vi/vim/nano/emacs didn't work.

Update 1: Ah shit `ps -aux` didn't work but `ps aux` did. Should have tried
tabbing in the first place!

# Done... or am I?

So after fixing the python script & killing the malware process, they let me
`sudo restart` the machine.

But then I still have no idea what this clue's about:

> When the firewall is all set up, dial this number to know what to do next:
> 777337777827778

Weird.
