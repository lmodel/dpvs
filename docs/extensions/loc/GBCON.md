---
search:
  boost: 10.0
---

# Class: GBCON 


_Concept representing region Cornwall (district) in country United_

_Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-CON](https://w3id.org/lmodel/dpv/loc/GB-CON)





```mermaid
 classDiagram
    class GBCON
    click GBCON href "../GBCON/"
      GB <|-- GBCON
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBCON**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-CON](https://w3id.org/lmodel/dpv/loc/GB-CON) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-CON
* Cornwall (district)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-CON |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-CON |
| native | loc:GBCON |
| exact | dpv_loc:GB-CON, dpv_loc_owl:GB-CON |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBCON
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-CON
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Cornwall (district) in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-CON
- Cornwall (district)
exact_mappings:
- dpv_loc:GB-CON
- dpv_loc_owl:GB-CON
is_a: GB
class_uri: loc:GB-CON

```
</details>

### Induced

<details>
```yaml
name: GBCON
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-CON
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Cornwall (district) in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-CON
- Cornwall (district)
exact_mappings:
- dpv_loc:GB-CON
- dpv_loc_owl:GB-CON
is_a: GB
class_uri: loc:GB-CON

```
</details></div>