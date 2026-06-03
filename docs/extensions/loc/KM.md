---
search:
  boost: 10.0
---

# Class: KM 


_Concept representing Country of Comoros_



<div data-search-exclude markdown="1">



URI: [loc:KM](https://w3id.org/lmodel/dpv/loc/KM)





```mermaid
 classDiagram
    class KM
    click KM href "../KM/"
      KM <|-- KMA
        click KMA href "../KMA/"
      KM <|-- KMG
        click KMG href "../KMG/"
      KM <|-- KMM
        click KMM href "../KMM/"
      
      
```





## Inheritance
* **KM**
    * [KMA](KMA.md)
    * [KMG](KMG.md)
    * [KMM](KMM.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:KM](https://w3id.org/lmodel/dpv/loc/KM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Comoros




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#KM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:KM |
| native | loc:KM |
| exact | dpv_loc:KM, dpv_loc_owl:KM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: KM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#KM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Comoros
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Comoros
exact_mappings:
- dpv_loc:KM
- dpv_loc_owl:KM
class_uri: loc:KM

```
</details>

### Induced

<details>
```yaml
name: KM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#KM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Comoros
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Comoros
exact_mappings:
- dpv_loc:KM
- dpv_loc_owl:KM
class_uri: loc:KM

```
</details></div>