---
title: lookatme.contrib.render
author: James Johnson
extensions:
  - image_ueberzug
  - render
styles:
  padding:
    left: 0
    right: 2
  margin:
    left: 2
    top: 3
    bottom: 2
    right: 2
---

# Graphviz Rendering

Source

~~~
```dot-15
graph ER {
    layout=neato
    node [shape=box]; terminal; markkown; images; awesome;
    node [shape=circle,style=filled,color=lightgrey]; lookatme;

    terminal -- lookatme;
    markkown -- lookatme;
    images -- lookatme;
    awesome -- lookatme;

    label = "\n\nLookatme & Graphviz";
    fontsize=10;
}
```
~~~

# Graphviz Rendering

Rendered, requires graphviz to be installed and the `dot` executable
to be in your `$PATH`

```dot-15
graph ER {
    layout=neato
    node [shape=box]; terminal; markdown; images; awesome;
    node [shape=circle,style=filled,color=lightgrey]; lookatme;

    terminal -- lookatme;
    markdown -- lookatme;
    images -- lookatme;
    awesome -- lookatme;

    label = "\n\nLookatme & Graphviz";
    fontsize=10;
}
```

# Mermaid JS Rendering

Source

~~~
```mermaid-15
graph TD
  A0 --> B
  A1 --> B
  B --> C
  C --> D
```
~~~

# Mermaid JS Rendering

Rendered. Requires mermaid-js to be installed and `mmdc` to be in your
`$PATH`.

```mermaid-15
graph TD
  A0 --> B
  A1 --> B
  B --> C
  C --> D
```
