---
search:
  boost: 10.0
---

# Class: GBNYM 


_Concept representing region Newry and Mourne District Council in country_

_United Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-NYM](https://w3id.org/lmodel/dpv/loc/GB-NYM)





```mermaid
 classDiagram
    class GBNYM
    click GBNYM href "../GBNYM/"
      GB <|-- GBNYM
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBNYM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-NYM](https://w3id.org/lmodel/dpv/loc/GB-NYM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-NYM
* Newry and Mourne District Council




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-NYM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-NYM |
| native | loc:GBNYM |
| exact | dpv_loc:GB-NYM, dpv_loc_owl:GB-NYM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBNYM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-NYM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Newry and Mourne District Council in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-NYM
- Newry and Mourne District Council
exact_mappings:
- dpv_loc:GB-NYM
- dpv_loc_owl:GB-NYM
is_a: GB
class_uri: loc:GB-NYM

```
</details>

### Induced

<details>
```yaml
name: GBNYM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-NYM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Newry and Mourne District Council in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-NYM
- Newry and Mourne District Council
exact_mappings:
- dpv_loc:GB-NYM
- dpv_loc_owl:GB-NYM
is_a: GB
class_uri: loc:GB-NYM

```
</details></div>