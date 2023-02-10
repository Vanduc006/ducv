f = open("index.html", "a")
hehe = '''
<h1 class='troll'>hoc vien lm tro meo cua vduc</h1>
<style>
    .troll {
        font-family: sans-serif;
        animation-name: color-troll;
        animation: color-troll 1s infinite;
    }
    @keyframes color-troll {
  0% {
    color: black;
  }
  25% {
    color: transparent;
  }
  50% {
    color: black;
  }
  75% {
    color: transparent;
  }
  100% {
    color: black;
  }
}
</style>'''
f.write(hehe)
f.close()
