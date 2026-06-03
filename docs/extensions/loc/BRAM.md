---
search:
  boost: 10.0
---

# Class: BRAM 


_Concept representing region Amazonas (Brazil) in country Brazil_



<div data-search-exclude markdown="1">



URI: [loc:BR-AM](https://w3id.org/lmodel/dpv/loc/BR-AM)





```mermaid
 classDiagram
    class BRAM
    click BRAM href "../BRAM/"
      BR <|-- BRAM
        click BR href "../BR/"
      
      
```





## Inheritance
* [BR](BR.md)
    * **BRAM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:BR-AM](https://w3id.org/lmodel/dpv/loc/BR-AM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* BR-AM
* Amazonas (Brazil)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#BR-AM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:BR-AM |
| native | loc:BRAM |
| exact | dpv_loc:BR-AM, dpv_loc_owl:BR-AM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BRAM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BR-AM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Amazonas (Brazil) in country Brazil
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BR-AM
- Amazonas (Brazil)
exact_mappings:
- dpv_loc:BR-AM
- dpv_loc_owl:BR-AM
is_a: BR
class_uri: loc:BR-AM

```
</details>

### Induced

<details>
```yaml
name: BRAM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BR-AM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Amazonas (Brazil) in country Brazil
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BR-AM
- Amazonas (Brazil)
exact_mappings:
- dpv_loc:BR-AM
- dpv_loc_owl:BR-AM
is_a: BR
class_uri: loc:BR-AM

```
</details></div>