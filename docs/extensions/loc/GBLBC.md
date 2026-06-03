---
search:
  boost: 10.0
---

# Class: GBLBC 


_Concept representing region Lisburn and Castlereagh in country United_

_Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-LBC](https://w3id.org/lmodel/dpv/loc/GB-LBC)





```mermaid
 classDiagram
    class GBLBC
    click GBLBC href "../GBLBC/"
      GB <|-- GBLBC
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBLBC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-LBC](https://w3id.org/lmodel/dpv/loc/GB-LBC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-LBC
* Lisburn and Castlereagh




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-LBC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-LBC |
| native | loc:GBLBC |
| exact | dpv_loc:GB-LBC, dpv_loc_owl:GB-LBC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBLBC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-LBC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Lisburn and Castlereagh in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-LBC
- Lisburn and Castlereagh
exact_mappings:
- dpv_loc:GB-LBC
- dpv_loc_owl:GB-LBC
is_a: GB
class_uri: loc:GB-LBC

```
</details>

### Induced

<details>
```yaml
name: GBLBC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-LBC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Lisburn and Castlereagh in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-LBC
- Lisburn and Castlereagh
exact_mappings:
- dpv_loc:GB-LBC
- dpv_loc_owl:GB-LBC
is_a: GB
class_uri: loc:GB-LBC

```
</details></div>