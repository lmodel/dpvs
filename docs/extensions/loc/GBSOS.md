---
search:
  boost: 10.0
---

# Class: GBSOS 


_Concept representing region Borough of Southend-on-Sea in country United_

_Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-SOS](https://w3id.org/lmodel/dpv/loc/GB-SOS)





```mermaid
 classDiagram
    class GBSOS
    click GBSOS href "../GBSOS/"
      GB <|-- GBSOS
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBSOS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-SOS](https://w3id.org/lmodel/dpv/loc/GB-SOS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-SOS
* Borough of Southend-on-Sea




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-SOS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-SOS |
| native | loc:GBSOS |
| exact | dpv_loc:GB-SOS, dpv_loc_owl:GB-SOS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBSOS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-SOS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Borough of Southend-on-Sea in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-SOS
- Borough of Southend-on-Sea
exact_mappings:
- dpv_loc:GB-SOS
- dpv_loc_owl:GB-SOS
is_a: GB
class_uri: loc:GB-SOS

```
</details>

### Induced

<details>
```yaml
name: GBSOS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-SOS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Borough of Southend-on-Sea in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-SOS
- Borough of Southend-on-Sea
exact_mappings:
- dpv_loc:GB-SOS
- dpv_loc_owl:GB-SOS
is_a: GB
class_uri: loc:GB-SOS

```
</details></div>