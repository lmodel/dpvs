---
search:
  boost: 10.0
---

# Class: FM 


_Concept representing Country of Micronesia (Federated States of)_



<div data-search-exclude markdown="1">



URI: [loc:FM](https://w3id.org/lmodel/dpv/loc/FM)





```mermaid
 classDiagram
    class FM
    click FM href "../FM/"
      FM <|-- FMPNI
        click FMPNI href "../FMPNI/"
      FM <|-- FMTRK
        click FMTRK href "../FMTRK/"
      FM <|-- FMYAP
        click FMYAP href "../FMYAP/"
      
      
```





## Inheritance
* **FM**
    * [FMPNI](FMPNI.md)
    * [FMTRK](FMTRK.md)
    * [FMYAP](FMYAP.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FM](https://w3id.org/lmodel/dpv/loc/FM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Micronesia (Federated States of)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FM |
| native | loc:FM |
| exact | dpv_loc:FM, dpv_loc_owl:FM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Micronesia (Federated States of)
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Micronesia (Federated States of)
exact_mappings:
- dpv_loc:FM
- dpv_loc_owl:FM
class_uri: loc:FM

```
</details>

### Induced

<details>
```yaml
name: FM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Micronesia (Federated States of)
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Micronesia (Federated States of)
exact_mappings:
- dpv_loc:FM
- dpv_loc_owl:FM
class_uri: loc:FM

```
</details></div>