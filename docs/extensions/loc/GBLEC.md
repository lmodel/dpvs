---
search:
  boost: 10.0
---

# Class: GBLEC 


_Concept representing region Leicestershire in country United Kingdom of_

_Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-LEC](https://w3id.org/lmodel/dpv/loc/GB-LEC)





```mermaid
 classDiagram
    class GBLEC
    click GBLEC href "../GBLEC/"
      GB <|-- GBLEC
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBLEC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-LEC](https://w3id.org/lmodel/dpv/loc/GB-LEC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-LEC
* Leicestershire




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-LEC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-LEC |
| native | loc:GBLEC |
| exact | dpv_loc:GB-LEC, dpv_loc_owl:GB-LEC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBLEC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-LEC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Leicestershire in country United Kingdom
  of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-LEC
- Leicestershire
exact_mappings:
- dpv_loc:GB-LEC
- dpv_loc_owl:GB-LEC
is_a: GB
class_uri: loc:GB-LEC

```
</details>

### Induced

<details>
```yaml
name: GBLEC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-LEC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Leicestershire in country United Kingdom
  of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-LEC
- Leicestershire
exact_mappings:
- dpv_loc:GB-LEC
- dpv_loc_owl:GB-LEC
is_a: GB
class_uri: loc:GB-LEC

```
</details></div>