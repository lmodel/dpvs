---
search:
  boost: 10.0
---

# Class: SexualPreference 


_Information about sexual preferences_



<div data-search-exclude markdown="1">



URI: [pd:SexualPreference](https://w3id.org/lmodel/dpv/pd/SexualPreference)





```mermaid
 classDiagram
    class SexualPreference
    click SexualPreference href "../SexualPreference/"
      Sexual <|-- SexualPreference
        click Sexual href "../Sexual/"
      
      
```





## Inheritance
* [Sexual](Sexual.md) [ [External](External.md)]
    * **SexualPreference**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:SexualPreference](https://w3id.org/lmodel/dpv/pd/SexualPreference) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Sexual Preference




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#SexualPreference |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:SexualPreference |
| native | pd:SexualPreference |
| exact | dpv_pd:SexualPreference, dpv_pd_owl:SexualPreference |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SexualPreference
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#SexualPreference
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about sexual preferences
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Sexual Preference
exact_mappings:
- dpv_pd:SexualPreference
- dpv_pd_owl:SexualPreference
is_a: Sexual
class_uri: pd:SexualPreference

```
</details>

### Induced

<details>
```yaml
name: SexualPreference
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#SexualPreference
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about sexual preferences
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Sexual Preference
exact_mappings:
- dpv_pd:SexualPreference
- dpv_pd_owl:SexualPreference
is_a: Sexual
class_uri: pd:SexualPreference

```
</details></div>