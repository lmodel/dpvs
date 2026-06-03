---
search:
  boost: 10.0
---

# Class: GBSAW 


_Concept representing region Metropolitan Borough of Sandwell in country_

_United Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-SAW](https://w3id.org/lmodel/dpv/loc/GB-SAW)





```mermaid
 classDiagram
    class GBSAW
    click GBSAW href "../GBSAW/"
      GB <|-- GBSAW
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBSAW**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-SAW](https://w3id.org/lmodel/dpv/loc/GB-SAW) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-SAW
* Metropolitan Borough of Sandwell




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-SAW |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-SAW |
| native | loc:GBSAW |
| exact | dpv_loc:GB-SAW, dpv_loc_owl:GB-SAW |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBSAW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-SAW
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Metropolitan Borough of Sandwell in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-SAW
- Metropolitan Borough of Sandwell
exact_mappings:
- dpv_loc:GB-SAW
- dpv_loc_owl:GB-SAW
is_a: GB
class_uri: loc:GB-SAW

```
</details>

### Induced

<details>
```yaml
name: GBSAW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-SAW
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Metropolitan Borough of Sandwell in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-SAW
- Metropolitan Borough of Sandwell
exact_mappings:
- dpv_loc:GB-SAW
- dpv_loc_owl:GB-SAW
is_a: GB
class_uri: loc:GB-SAW

```
</details></div>