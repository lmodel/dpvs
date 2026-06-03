---
search:
  boost: 10.0
---

# Class: GBHAV 


_Concept representing region London Borough of Havering in country United_

_Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-HAV](https://w3id.org/lmodel/dpv/loc/GB-HAV)





```mermaid
 classDiagram
    class GBHAV
    click GBHAV href "../GBHAV/"
      GB <|-- GBHAV
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBHAV**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-HAV](https://w3id.org/lmodel/dpv/loc/GB-HAV) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-HAV
* London Borough of Havering




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-HAV |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-HAV |
| native | loc:GBHAV |
| exact | dpv_loc:GB-HAV, dpv_loc_owl:GB-HAV |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBHAV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-HAV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Havering in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-HAV
- London Borough of Havering
exact_mappings:
- dpv_loc:GB-HAV
- dpv_loc_owl:GB-HAV
is_a: GB
class_uri: loc:GB-HAV

```
</details>

### Induced

<details>
```yaml
name: GBHAV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-HAV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Havering in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-HAV
- London Borough of Havering
exact_mappings:
- dpv_loc:GB-HAV
- dpv_loc_owl:GB-HAV
is_a: GB
class_uri: loc:GB-HAV

```
</details></div>