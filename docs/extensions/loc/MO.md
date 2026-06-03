---
search:
  boost: 10.0
---

# Class: MO 


_Concept representing Country of Macao_



<div data-search-exclude markdown="1">



URI: [loc:MO](https://w3id.org/lmodel/dpv/loc/MO)





```mermaid
 classDiagram
    class MO
    click MO href "../MO/"
      CN <|-- MO
        click CN href "../CN/"
      
      
```





## Inheritance
* [CN](CN.md)
    * **MO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:MO](https://w3id.org/lmodel/dpv/loc/MO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* China, Macao Special Administrative Region




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#MO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:MO |
| native | loc:MO |
| exact | dpv_loc:MO, dpv_loc_owl:MO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Macao
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- China, Macao Special Administrative Region
exact_mappings:
- dpv_loc:MO
- dpv_loc_owl:MO
is_a: CN
class_uri: loc:MO

```
</details>

### Induced

<details>
```yaml
name: MO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Macao
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- China, Macao Special Administrative Region
exact_mappings:
- dpv_loc:MO
- dpv_loc_owl:MO
is_a: CN
class_uri: loc:MO

```
</details></div>