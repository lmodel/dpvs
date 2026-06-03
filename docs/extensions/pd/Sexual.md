---
search:
  boost: 10.0
---

# Class: Sexual 


_Information about sexuality and sexual history_



<div data-search-exclude markdown="1">



URI: [pd:Sexual](https://w3id.org/lmodel/dpv/pd/Sexual)





```mermaid
 classDiagram
    class Sexual
    click Sexual href "../Sexual/"
      External <|-- Sexual
        click External href "../External/"
      

      Sexual <|-- Fetish
        click Fetish href "../Fetish/"
      Sexual <|-- Proclivity
        click Proclivity href "../Proclivity/"
      Sexual <|-- SexualHistory
        click SexualHistory href "../SexualHistory/"
      Sexual <|-- SexualPreference
        click SexualPreference href "../SexualPreference/"
      

      
```





## Inheritance
* **Sexual** [ [External](External.md)]
    * [Fetish](Fetish.md)
    * [Proclivity](Proclivity.md)
    * [SexualHistory](SexualHistory.md)
    * [SexualPreference](SexualPreference.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Sexual](https://w3id.org/lmodel/dpv/pd/Sexual) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Sexual




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Sexual |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Sexual |
| native | pd:Sexual |
| exact | dpv_pd:Sexual, dpv_pd_owl:Sexual |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Sexual
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Sexual
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about sexuality and sexual history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Sexual
exact_mappings:
- dpv_pd:Sexual
- dpv_pd_owl:Sexual
mixins:
- External
class_uri: pd:Sexual

```
</details>

### Induced

<details>
```yaml
name: Sexual
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Sexual
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about sexuality and sexual history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Sexual
exact_mappings:
- dpv_pd:Sexual
- dpv_pd_owl:Sexual
mixins:
- External
class_uri: pd:Sexual

```
</details></div>