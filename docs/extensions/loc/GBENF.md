---
search:
  boost: 10.0
---

# Class: GBENF 


_Concept representing region London Borough of Enfield in country United_

_Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-ENF](https://w3id.org/lmodel/dpv/loc/GB-ENF)





```mermaid
 classDiagram
    class GBENF
    click GBENF href "../GBENF/"
      GB <|-- GBENF
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBENF**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-ENF](https://w3id.org/lmodel/dpv/loc/GB-ENF) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-ENF
* London Borough of Enfield




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-ENF |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-ENF |
| native | loc:GBENF |
| exact | dpv_loc:GB-ENF, dpv_loc_owl:GB-ENF |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBENF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-ENF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Enfield in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-ENF
- London Borough of Enfield
exact_mappings:
- dpv_loc:GB-ENF
- dpv_loc_owl:GB-ENF
is_a: GB
class_uri: loc:GB-ENF

```
</details>

### Induced

<details>
```yaml
name: GBENF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-ENF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Enfield in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-ENF
- London Borough of Enfield
exact_mappings:
- dpv_loc:GB-ENF
- dpv_loc_owl:GB-ENF
is_a: GB
class_uri: loc:GB-ENF

```
</details></div>