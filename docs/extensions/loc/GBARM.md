---
search:
  boost: 10.0
---

# Class: GBARM 


_Concept representing region Armagh City and District Council in country_

_United Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-ARM](https://w3id.org/lmodel/dpv/loc/GB-ARM)





```mermaid
 classDiagram
    class GBARM
    click GBARM href "../GBARM/"
      GB <|-- GBARM
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBARM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-ARM](https://w3id.org/lmodel/dpv/loc/GB-ARM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-ARM
* Armagh City and District Council




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-ARM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-ARM |
| native | loc:GBARM |
| exact | dpv_loc:GB-ARM, dpv_loc_owl:GB-ARM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBARM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-ARM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Armagh City and District Council in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-ARM
- Armagh City and District Council
exact_mappings:
- dpv_loc:GB-ARM
- dpv_loc_owl:GB-ARM
is_a: GB
class_uri: loc:GB-ARM

```
</details>

### Induced

<details>
```yaml
name: GBARM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-ARM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Armagh City and District Council in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-ARM
- Armagh City and District Council
exact_mappings:
- dpv_loc:GB-ARM
- dpv_loc_owl:GB-ARM
is_a: GB
class_uri: loc:GB-ARM

```
</details></div>