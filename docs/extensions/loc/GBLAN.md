---
search:
  boost: 10.0
---

# Class: GBLAN 


_Concept representing region Lancashire in country United Kingdom of_

_Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-LAN](https://w3id.org/lmodel/dpv/loc/GB-LAN)





```mermaid
 classDiagram
    class GBLAN
    click GBLAN href "../GBLAN/"
      GB <|-- GBLAN
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBLAN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-LAN](https://w3id.org/lmodel/dpv/loc/GB-LAN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-LAN
* Lancashire




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-LAN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-LAN |
| native | loc:GBLAN |
| exact | dpv_loc:GB-LAN, dpv_loc_owl:GB-LAN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBLAN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-LAN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Lancashire in country United Kingdom of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-LAN
- Lancashire
exact_mappings:
- dpv_loc:GB-LAN
- dpv_loc_owl:GB-LAN
is_a: GB
class_uri: loc:GB-LAN

```
</details>

### Induced

<details>
```yaml
name: GBLAN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-LAN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Lancashire in country United Kingdom of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-LAN
- Lancashire
exact_mappings:
- dpv_loc:GB-LAN
- dpv_loc_owl:GB-LAN
is_a: GB
class_uri: loc:GB-LAN

```
</details></div>