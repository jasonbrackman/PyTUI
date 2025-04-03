Create a text based UI around the abstract concepts of widgets and layouts.

Example Code:
  h_layout = TableLayout()
  h_layout.add_coloumn(Widget(list("abcdefgh"), padding=2), "Letters")
  h_layout.add_coloumn(Widget(["asdf", 'were', 'fizz', 'buzz', 'bang', '23432', 'vxXxv'], alignment=Alignment.CENTER, padding=8), "Words")
  h_layout.add_coloumn(Widget(list("ABCDEFGHIJK"), padding=2), "Caps")
  h_layout.add_coloumn(Widget(["Super", "Cali", "Fragilistic"], padding=2), "Magic")

  v_layout = VLayout()
  v_layout.add(Widget(list(["Example Display"]), alignment=Alignment.CENTER, padding=2))
  v_layout.add(h_layout)
  v_layout.add(Widget(list(["Example Footer"]), alignment=Alignment.CENTER, padding=2))

  v_layout.render()

```
┌────────────────────────────────────────────┐
│              Example Display               │
├────────────────────────────────────────────┤
│Letters  │    Words    │Caps  │Magic        │
├────────────────────────────────────────────┤
│a        │    asdf     │A     │Super        │
│b        │    were     │B     │Cali         │
│c        │    fizz     │C     │Fragilistic  │
│d        │    buzz     │D     │             │
│e        │    bang     │E     │             │
│f        │    23432    │F     │             │
│g        │    vxXxv    │G     │             │
│h        │             │H     │             │
│         │             │I     │             │
│         │             │J     │             │
│         │             │K     │             │
├────────────────────────────────────────────┤
│               Example Footer               │
└────────────────────────────────────────────┘
```
