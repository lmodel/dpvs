---
search:
  boost: 10.0
---

# Class: GBSOM 


_Concept representing region Somerset in country United Kingdom of Great_

_Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-SOM](https://w3id.org/lmodel/dpv/loc/GB-SOM)





```mermaid
 classDiagram
    class GBSOM
    click GBSOM href "../GBSOM/"
      GB <|-- GBSOM
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBSOM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-SOM](https://w3id.org/lmodel/dpv/loc/GB-SOM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-SOM
* Somerset




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-SOM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-SOM |
| native | loc:GBSOM |
| exact | dpv_loc:GB-SOM, dpv_loc_owl:GB-SOM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBSOM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-SOM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Somerset in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-SOM
- Somerset
exact_mappings:
- dpv_loc:GB-SOM
- dpv_loc_owl:GB-SOM
is_a: GB
class_uri: loc:GB-SOM

```
</details>

### Induced

<details>
```yaml
name: GBSOM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-SOM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Somerset in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-SOM
- Somerset
exact_mappings:
- dpv_loc:GB-SOM
- dpv_loc_owl:GB-SOM
is_a: GB
class_uri: loc:GB-SOM

```
</details></div>