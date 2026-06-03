---
search:
  boost: 10.0
---

# Class: GBBEN 


_Concept representing region London Borough of Brent in country United_

_Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-BEN](https://w3id.org/lmodel/dpv/loc/GB-BEN)





```mermaid
 classDiagram
    class GBBEN
    click GBBEN href "../GBBEN/"
      GB <|-- GBBEN
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBBEN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-BEN](https://w3id.org/lmodel/dpv/loc/GB-BEN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-BEN
* London Borough of Brent




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-BEN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-BEN |
| native | loc:GBBEN |
| exact | dpv_loc:GB-BEN, dpv_loc_owl:GB-BEN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBBEN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-BEN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Brent in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-BEN
- London Borough of Brent
exact_mappings:
- dpv_loc:GB-BEN
- dpv_loc_owl:GB-BEN
is_a: GB
class_uri: loc:GB-BEN

```
</details>

### Induced

<details>
```yaml
name: GBBEN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-BEN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Brent in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-BEN
- London Borough of Brent
exact_mappings:
- dpv_loc:GB-BEN
- dpv_loc_owl:GB-BEN
is_a: GB
class_uri: loc:GB-BEN

```
</details></div>