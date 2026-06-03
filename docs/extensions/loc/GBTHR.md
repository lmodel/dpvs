---
search:
  boost: 10.0
---

# Class: GBTHR 


_Concept representing region Thurrock in country United Kingdom of Great_

_Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-THR](https://w3id.org/lmodel/dpv/loc/GB-THR)





```mermaid
 classDiagram
    class GBTHR
    click GBTHR href "../GBTHR/"
      GB <|-- GBTHR
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBTHR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-THR](https://w3id.org/lmodel/dpv/loc/GB-THR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-THR
* Thurrock




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-THR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-THR |
| native | loc:GBTHR |
| exact | dpv_loc:GB-THR, dpv_loc_owl:GB-THR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBTHR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-THR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Thurrock in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-THR
- Thurrock
exact_mappings:
- dpv_loc:GB-THR
- dpv_loc_owl:GB-THR
is_a: GB
class_uri: loc:GB-THR

```
</details>

### Induced

<details>
```yaml
name: GBTHR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-THR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Thurrock in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-THR
- Thurrock
exact_mappings:
- dpv_loc:GB-THR
- dpv_loc_owl:GB-THR
is_a: GB
class_uri: loc:GB-THR

```
</details></div>