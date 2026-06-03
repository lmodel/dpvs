---
search:
  boost: 10.0
---

# Class: TG 


_Concept representing Country of Togo_



<div data-search-exclude markdown="1">



URI: [loc:TG](https://w3id.org/lmodel/dpv/loc/TG)





```mermaid
 classDiagram
    class TG
    click TG href "../TG/"
      TG <|-- TGK
        click TGK href "../TGK/"
      TG <|-- TGM
        click TGM href "../TGM/"
      TG <|-- TGP
        click TGP href "../TGP/"
      
      
```





## Inheritance
* **TG**
    * [TGK](TGK.md)
    * [TGM](TGM.md)
    * [TGP](TGP.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:TG](https://w3id.org/lmodel/dpv/loc/TG) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Togo




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#TG |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:TG |
| native | loc:TG |
| exact | dpv_loc:TG, dpv_loc_owl:TG |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#TG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Togo
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Togo
exact_mappings:
- dpv_loc:TG
- dpv_loc_owl:TG
class_uri: loc:TG

```
</details>

### Induced

<details>
```yaml
name: TG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#TG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Togo
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Togo
exact_mappings:
- dpv_loc:TG
- dpv_loc_owl:TG
class_uri: loc:TG

```
</details></div>