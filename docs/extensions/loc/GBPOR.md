---
search:
  boost: 10.0
---

# Class: GBPOR 


_Concept representing region Portsmouth in country United Kingdom of_

_Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-POR](https://w3id.org/lmodel/dpv/loc/GB-POR)





```mermaid
 classDiagram
    class GBPOR
    click GBPOR href "../GBPOR/"
      GB <|-- GBPOR
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBPOR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-POR](https://w3id.org/lmodel/dpv/loc/GB-POR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-POR
* Portsmouth




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-POR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-POR |
| native | loc:GBPOR |
| exact | dpv_loc:GB-POR, dpv_loc_owl:GB-POR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBPOR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-POR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Portsmouth in country United Kingdom of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-POR
- Portsmouth
exact_mappings:
- dpv_loc:GB-POR
- dpv_loc_owl:GB-POR
is_a: GB
class_uri: loc:GB-POR

```
</details>

### Induced

<details>
```yaml
name: GBPOR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-POR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Portsmouth in country United Kingdom of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-POR
- Portsmouth
exact_mappings:
- dpv_loc:GB-POR
- dpv_loc_owl:GB-POR
is_a: GB
class_uri: loc:GB-POR

```
</details></div>