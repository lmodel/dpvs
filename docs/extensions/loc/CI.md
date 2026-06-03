---
search:
  boost: 10.0
---

# Class: CI 


_Concept representing Country of Côte d’Ivoire_



<div data-search-exclude markdown="1">



URI: [loc:CI](https://w3id.org/lmodel/dpv/loc/CI)





```mermaid
 classDiagram
    class CI
    click CI href "../CI/"
      CI <|-- CI05
        click CI05 href "../CI05/"
      CI <|-- CIAB
        click CIAB href "../CIAB/"
      CI <|-- CIDN
        click CIDN href "../CIDN/"
      CI <|-- CIYM
        click CIYM href "../CIYM/"
      
      
```





## Inheritance
* **CI**
    * [CI05](CI05.md)
    * [CIAB](CIAB.md)
    * [CIDN](CIDN.md)
    * [CIYM](CIYM.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:CI](https://w3id.org/lmodel/dpv/loc/CI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Côte d’Ivoire




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#CI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:CI |
| native | loc:CI |
| exact | dpv_loc:CI, dpv_loc_owl:CI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Côte d’Ivoire
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Côte d’Ivoire
exact_mappings:
- dpv_loc:CI
- dpv_loc_owl:CI
class_uri: loc:CI

```
</details>

### Induced

<details>
```yaml
name: CI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Côte d’Ivoire
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Côte d’Ivoire
exact_mappings:
- dpv_loc:CI
- dpv_loc_owl:CI
class_uri: loc:CI

```
</details></div>