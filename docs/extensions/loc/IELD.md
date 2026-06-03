---
search:
  boost: 10.0
---

# Class: IELD 


_Concept representing region County Longford in country Ireland_



<div data-search-exclude markdown="1">



URI: [loc:IE-LD](https://w3id.org/lmodel/dpv/loc/IE-LD)





```mermaid
 classDiagram
    class IELD
    click IELD href "../IELD/"
      IE <|-- IELD
        click IE href "../IE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IE](IE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **IELD**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IE-LD](https://w3id.org/lmodel/dpv/loc/IE-LD) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IE-LD
* County Longford




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IE-LD |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IE-LD |
| native | loc:IELD |
| exact | dpv_loc:IE-LD, dpv_loc_owl:IE-LD |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IELD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-LD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Longford in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-LD
- County Longford
exact_mappings:
- dpv_loc:IE-LD
- dpv_loc_owl:IE-LD
is_a: IE
class_uri: loc:IE-LD

```
</details>

### Induced

<details>
```yaml
name: IELD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-LD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Longford in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-LD
- County Longford
exact_mappings:
- dpv_loc:IE-LD
- dpv_loc_owl:IE-LD
is_a: IE
class_uri: loc:IE-LD

```
</details></div>