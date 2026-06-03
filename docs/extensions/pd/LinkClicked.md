---
search:
  boost: 10.0
---

# Class: LinkClicked 


_Information about the links that an individual has clicked_



<div data-search-exclude markdown="1">



URI: [pd:LinkClicked](https://w3id.org/lmodel/dpv/pd/LinkClicked)





```mermaid
 classDiagram
    class LinkClicked
    click LinkClicked href "../LinkClicked/"
      Behavioural <|-- LinkClicked
        click Behavioural href "../Behavioural/"
      
      
```





## Inheritance
* [External](External.md)
    * [Behavioural](Behavioural.md)
        * **LinkClicked**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:LinkClicked](https://w3id.org/lmodel/dpv/pd/LinkClicked) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Link Clicked




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#LinkClicked |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:LinkClicked |
| native | pd:LinkClicked |
| exact | dpv_pd:LinkClicked, dpv_pd_owl:LinkClicked |
| related | svd:Navigation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LinkClicked
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#LinkClicked
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about the links that an individual has clicked
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Link Clicked
exact_mappings:
- dpv_pd:LinkClicked
- dpv_pd_owl:LinkClicked
related_mappings:
- svd:Navigation
is_a: Behavioural
class_uri: pd:LinkClicked

```
</details>

### Induced

<details>
```yaml
name: LinkClicked
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#LinkClicked
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about the links that an individual has clicked
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Link Clicked
exact_mappings:
- dpv_pd:LinkClicked
- dpv_pd_owl:LinkClicked
related_mappings:
- svd:Navigation
is_a: Behavioural
class_uri: pd:LinkClicked

```
</details></div>