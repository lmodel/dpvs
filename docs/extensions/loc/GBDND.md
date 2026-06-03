---
search:
  boost: 10.0
---

# Class: GBDND 


_Concept representing region Dundee in country United Kingdom of Great_

_Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-DND](https://w3id.org/lmodel/dpv/loc/GB-DND)





```mermaid
 classDiagram
    class GBDND
    click GBDND href "../GBDND/"
      GB <|-- GBDND
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBDND**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-DND](https://w3id.org/lmodel/dpv/loc/GB-DND) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-DND
* Dundee




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-DND |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-DND |
| native | loc:GBDND |
| exact | dpv_loc:GB-DND, dpv_loc_owl:GB-DND |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBDND
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-DND
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Dundee in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-DND
- Dundee
exact_mappings:
- dpv_loc:GB-DND
- dpv_loc_owl:GB-DND
is_a: GB
class_uri: loc:GB-DND

```
</details>

### Induced

<details>
```yaml
name: GBDND
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-DND
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Dundee in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-DND
- Dundee
exact_mappings:
- dpv_loc:GB-DND
- dpv_loc_owl:GB-DND
is_a: GB
class_uri: loc:GB-DND

```
</details></div>