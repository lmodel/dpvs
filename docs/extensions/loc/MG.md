---
search:
  boost: 10.0
---

# Class: MG 


_Concept representing Country of Madagascar_



<div data-search-exclude markdown="1">



URI: [loc:MG](https://w3id.org/lmodel/dpv/loc/MG)





```mermaid
 classDiagram
    class MG
    click MG href "../MG/"
      MG <|-- MGA
        click MGA href "../MGA/"
      MG <|-- MGD
        click MGD href "../MGD/"
      MG <|-- MGF
        click MGF href "../MGF/"
      MG <|-- MGM
        click MGM href "../MGM/"
      MG <|-- MGT
        click MGT href "../MGT/"
      
      
```





## Inheritance
* **MG**
    * [MGA](MGA.md)
    * [MGD](MGD.md)
    * [MGF](MGF.md)
    * [MGM](MGM.md)
    * [MGT](MGT.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:MG](https://w3id.org/lmodel/dpv/loc/MG) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Madagascar




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#MG |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:MG |
| native | loc:MG |
| exact | dpv_loc:MG, dpv_loc_owl:MG |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Madagascar
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Madagascar
exact_mappings:
- dpv_loc:MG
- dpv_loc_owl:MG
class_uri: loc:MG

```
</details>

### Induced

<details>
```yaml
name: MG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Madagascar
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Madagascar
exact_mappings:
- dpv_loc:MG
- dpv_loc_owl:MG
class_uri: loc:MG

```
</details></div>