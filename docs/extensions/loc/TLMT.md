---
search:
  boost: 10.0
---

# Class: TLMT 


_Concept representing region Manatuto (Municipality) in country_

_Timor-Leste_



<div data-search-exclude markdown="1">



URI: [loc:TL-MT](https://w3id.org/lmodel/dpv/loc/TL-MT)





```mermaid
 classDiagram
    class TLMT
    click TLMT href "../TLMT/"
      TL <|-- TLMT
        click TL href "../TL/"
      
      
```





## Inheritance
* [TL](TL.md)
    * **TLMT**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:TL-MT](https://w3id.org/lmodel/dpv/loc/TL-MT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* TL-MT
* Manatuto (Municipality)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#TL-MT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:TL-MT |
| native | loc:TLMT |
| exact | dpv_loc:TL-MT, dpv_loc_owl:TL-MT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TLMT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#TL-MT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Manatuto (Municipality) in country

  Timor-Leste'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- TL-MT
- Manatuto (Municipality)
exact_mappings:
- dpv_loc:TL-MT
- dpv_loc_owl:TL-MT
is_a: TL
class_uri: loc:TL-MT

```
</details>

### Induced

<details>
```yaml
name: TLMT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#TL-MT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Manatuto (Municipality) in country

  Timor-Leste'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- TL-MT
- Manatuto (Municipality)
exact_mappings:
- dpv_loc:TL-MT
- dpv_loc_owl:TL-MT
is_a: TL
class_uri: loc:TL-MT

```
</details></div>