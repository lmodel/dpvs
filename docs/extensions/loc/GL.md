---
search:
  boost: 10.0
---

# Class: GL 


_Concept representing Country of Greenland_



<div data-search-exclude markdown="1">



URI: [loc:GL](https://w3id.org/lmodel/dpv/loc/GL)





```mermaid
 classDiagram
    class GL
    click GL href "../GL/"
      GL <|-- GLAV
        click GLAV href "../GLAV/"
      GL <|-- GLKU
        click GLKU href "../GLKU/"
      GL <|-- GLQA
        click GLQA href "../GLQA/"
      GL <|-- GLQE
        click GLQE href "../GLQE/"
      GL <|-- GLQT
        click GLQT href "../GLQT/"
      GL <|-- GLSM
        click GLSM href "../GLSM/"
      
      
```





## Inheritance
* **GL**
    * [GLAV](GLAV.md)
    * [GLKU](GLKU.md)
    * [GLQA](GLQA.md)
    * [GLQE](GLQE.md)
    * [GLQT](GLQT.md)
    * [GLSM](GLSM.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GL](https://w3id.org/lmodel/dpv/loc/GL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Greenland




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GL |
| native | loc:GL |
| exact | dpv_loc:GL, dpv_loc_owl:GL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Greenland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Greenland
exact_mappings:
- dpv_loc:GL
- dpv_loc_owl:GL
class_uri: loc:GL

```
</details>

### Induced

<details>
```yaml
name: GL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Greenland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Greenland
exact_mappings:
- dpv_loc:GL
- dpv_loc_owl:GL
class_uri: loc:GL

```
</details></div>